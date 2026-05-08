# GetPathName Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName`

Gets the full path name for this component.
Gets the full path name for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPathName() As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
value = instance.GetPathName()
```

```

System.string GetPathName()
```

```

System.String^ GetPathName(); 
```

#### Return Value

Full path name for this component, including the filename

Remarks

The underlying document for this component might not have been loaded into memory if the component is lightweight or suppressed. In this situation, [IComponent2::GetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc.md) or [IComponent2::IGetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelDoc.md) may return NULL and the file and path name returned by this method will be the As-Saved file and path name for the IComponent2.

This method does not apply search criteria or look in the current working directory for the component file reference if the component is lightweight or suppressed.

Example

[Get Component for Selected Entity (VBA)](Get_Component_for_Selected_Entity_Example_VB.htm)  
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)  
[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)  
[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)  
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.md)  
[IComponent2::GetImportedPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetImportedPath.md)
