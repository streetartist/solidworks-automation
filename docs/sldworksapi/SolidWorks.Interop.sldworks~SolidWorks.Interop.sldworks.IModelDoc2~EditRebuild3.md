# EditRebuild3 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3`

Rebuilds only those features that need to be rebuilt in the active configuration in the model.
Rebuilds only those features that need to be rebuilt in the active configuration in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditRebuild3() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.EditRebuild3()
```

```

System.bool EditRebuild3()
```

```

System.bool EditRebuild3(); 
```

#### Return Value

True if only those features that need to be rebuilt are rebuilt in the active configuration in the model, false if not

Remarks

This method only works in-context of the active document.

Example

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)  
[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)  
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Rebuild Model (VBA)](Rebuild_Example_VB.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Modify Surface-cut Feature (C#)](Modify_Surface_Cut_Feature_Example_CSharp.htm)  
[Modify Surface-cut Feature (VB.NET)](Modify_Surface_Cut_Feature_Example_VBNET.htm)  
[Modify Surface-cut Feature (VBA)](Modify_Surface_Cut_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)  
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)  
[IConfiguration::AddRebuildSaveMark Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.md)  
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.md)
