# ProfileOffsetDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileOffsetDistance`

Gets or sets the offset distance of the profile for this gusset feature.
Gets or sets the offset distance of the profile for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileOffsetDistance As System.Double
```

```

Dim instance As IGussetFeatureData
Dim value As System.Double
 
instance.ProfileOffsetDistance = value
 
value = instance.ProfileOffsetDistance
```

```

System.double ProfileOffsetDistance {get; set;}
```

```

property System.double ProfileOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance

Remarks

[IGussetFeatureData::OffsetUsed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~OffsetUsed.md) must be set to True.

Example

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)  
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)  
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
