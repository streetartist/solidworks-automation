# D2OffsetReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2OffsetReference`

Obsolete. Superseded by IBaseFlangeFeatureData::D2EndConditionReference.
Obsolete. Superseded by [IBaseFlangeFeatureData::D2EndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2EndConditionReference.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2OffsetReference As System.Object
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Object
 
instance.D2OffsetReference = value
 
value = instance.D2OffsetReference
```

```

System.object D2OffsetReference {get; set;}
```

```

property System.Object^ D2OffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pointer to the offset reference

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::D1OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1OffsetReference.md)
