# OffsetUsed Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~OffsetUsed`

Gets or sets whether offset is used to locate the profile for this gusset feature.
Gets or sets whether offset is used to locate the profile for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetUsed As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim value As System.Boolean
 
instance.OffsetUsed = value
 
value = instance.OffsetUsed
```

```

System.bool OffsetUsed {get; set;}
```

```

property System.bool OffsetUsed {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if offset is used, false if not

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
