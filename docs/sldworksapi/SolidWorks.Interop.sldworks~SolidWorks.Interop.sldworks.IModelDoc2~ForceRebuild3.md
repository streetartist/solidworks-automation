# ForceRebuild3 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3`

Forces a rebuild of all features in the active configuration in the model.
Forces a rebuild of all features in the active configuration in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ForceRebuild3( _
   ByVal TopOnly As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim TopOnly As System.Boolean
Dim value As System.Boolean
 
value = instance.ForceRebuild3(TopOnly)
```

```

System.bool ForceRebuild3( 
   System.bool TopOnly
)
```

```

System.bool ForceRebuild3( 
   System.bool TopOnly
) 
```

#### Parameters

*TopOnly*
:   True rebuilds the top-level assembly only; false rebuilds the top-level assembly and all subassemblies

#### Return Value

True if all features in the active configuration at the specified assembly level in the model are rebuilt, false if not

Example

[Force Rebuild (VBA)](Force_Rebuild_Example_VB.htm)  
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)  
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)  
[Rebuild Model (VBA)](Rebuild_Example_VB.htm)  
[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)  
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)  
[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.md)  
[IModelDoc2::ShowFeatureErrorDialog Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.md)  
[IConfiguration::AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.md)  
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)
