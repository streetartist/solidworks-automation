# IGroundPlaneFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData`

Allows access to a ground plane feature.
Allows access to a ground plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IGroundPlaneFeatureData 
```

```

Dim instance As IGroundPlaneFeatureData
```

```

public interface IGroundPlaneFeatureData 
```

```

public interface class IGroundPlaneFeatureData 
```

Remarks

Use this interface to insert a ground plane at each level of a plant assembly. Ground planes are used as reference geometry when inserting published assets at each level.

Call [IAssemblyDoc::ActivateGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.md) to activate the ground plane on the level where you want to insert a published asset; the asset's ground face snaps to the assembly's activated ground plane. Components with magnetic mates snap only to components that are also on the active ground plane.

Only one ground plane can be active at a given time in each assembly configuration.

See **Large Assemblies > Facility Layout** in the SOLIDWORKS user-interface help.

Example

'VBA

'==========================================================================

'1. Ensure that the specified model exists.  
'2. Run the macro.  
'3. Creates **Ground Plane1** in the Ground Planes folder of  
'    the FeatureManager design tree and modifies it.  
'===========================================================================

Dim swApp As SldWorks.SldWorks  
Dim featmgr As SldWorks.FeatureManager  
Dim swGPData As SldWorks.GroundPlaneFeatureData  
Dim featdata As SldWorks.GroundPlaneFeatureData  
Dim ent As SldWorks.Face2  
Dim feat As SldWorks.Feature  
Dim Part As SldWorks.ModelDoc2  
Dim swAssembly As SldWorks.AssemblyDoc  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
Option Explicit

Sub main()

> Set swApp = Application.SldWorks  
>   
> Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem2.sldasm", 2, 0, "", longstatus, longwarnings)  
>   
> Set swAssembly = Part  
> swApp.ActivateDoc2 "assem2.sldasm", False, longstatus  
> Set Part = swApp.ActiveDoc  
> Set featmgr = Part.FeatureManager  
>   
> boolstatus = Part.Extension.SelectByRay(-0.124913770805165, 0.118854842937424, 7.02747343940473E-02, -0.620586476260429, -0.617739368127351, -0.482980846978724, 3.09726603088958E-03, 2, True, 0, 0)  
>   
> Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Set swGPData = featmgr.**CreateDefinition**(swFmGroundPlane)  
> swGPData.**PlanarEntity** = ent  
>   
> Set feat = featmgr.**CreateFeature**(swGPData)  
> Part.ClearSelection2 True  
> Set featdata = feat.**GetDefinition**()  
> boolstatus = Part.Extension.SelectByRay(0.119119826446138, 5.16103810082313E-03, 0.183494239718641, -0.620586476260429, -0.617739368127351, -0.482980846978724, 3.09726603088958E-03, 2, False, 0, 0)  
> Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)  
> featdata.**AccessSelections** Part, Nothing  
>   
> featdata.**PlanarEntity** = ent  
> feat.**ModifyDefinition** featdata, Part, Nothing

End Sub

Example

[Create Ground Plane (C#)](Create_Ground_Plane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
