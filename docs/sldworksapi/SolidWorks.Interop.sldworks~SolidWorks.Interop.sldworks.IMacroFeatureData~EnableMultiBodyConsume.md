# EnableMultiBodyConsume Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume`

Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature.
Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableMultiBodyConsume As System.Boolean
```

```

Dim instance As IMacroFeatureData
Dim value As System.Boolean
 
instance.EnableMultiBodyConsume = value
 
value = instance.EnableMultiBodyConsume
```

```

System.bool EnableMultiBodyConsume {get; set;}
```

```

property System.bool EnableMultiBodyConsume {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to replace the original edit body with multiple solid bodies, false to not

Remarks

This method was designed to work specifically with macro features that generate multiple solid bodies. The [rebuild](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) function of a macro feature creates or regenerates the macro feature in the FeatureManager design tree. By default, if the rebuild function creates multiple solid bodies, it appends the new solid bodies to the original edit body in the Solid Bodies folder of the FeatureManager design tree.

Always set this property to true in the rebuild function when working with macro features involving multiple input or output bodies.

Example

[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)  
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)  
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEditBodiesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.md)  
[IMacroFeatureData::IGetEditBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md)  
[IMacroFeatureData::EditBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md)
