# EditBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies`

Gets or sets the bodies to be modified by this macro feature.
Gets or sets the bodies to be modified by this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditBodies As System.Object
```

```

Dim instance As IMacroFeatureData
Dim value As System.Object
 
instance.EditBodies = value
 
value = instance.EditBodies
```

```

System.object EditBodies {get; set;}
```

```

property System.Object^ EditBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEditBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.md)  
[IMacroFeatureData::IGetEditBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md)  
[IMacroFeatureData::ISetEditBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.md)  
[IMacroFeatureData::EnableMultiBodyConsume Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.md)
