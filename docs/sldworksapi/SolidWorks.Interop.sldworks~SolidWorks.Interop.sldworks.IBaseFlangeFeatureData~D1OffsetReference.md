# D1OffsetReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1OffsetReference`

Obsolete. Superseded by IBaseFlangeFeatureData::D1EndConditionReference.
Obsolete. Superseded by [IBaseFlangeFeatureData::D1EndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1EndConditionReference.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1OffsetReference As System.Object
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Object
 
instance.D1OffsetReference = value
 
value = instance.D1OffsetReference
```

```

System.object D1OffsetReference {get; set;}
```

```

property System.Object^ D1OffsetReference {
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
[IBaseFlangeFeatureData::D2OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2OffsetReference.md)
