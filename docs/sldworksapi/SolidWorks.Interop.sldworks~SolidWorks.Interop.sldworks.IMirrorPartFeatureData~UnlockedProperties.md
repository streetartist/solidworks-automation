# UnlockedProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnlockedProperties`

Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part.
Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UnlockedProperties As System.Boolean
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean
 
instance.UnlockedProperties = value
 
value = instance.UnlockedProperties
```

```

System.bool UnlockedProperties {get; set;}
```

```

property System.bool UnlockedProperties {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable editing of the sheet-metal definition in this mirrored sheet-metal part, false to not

Remarks

[IMirrorPartFeatureData::SheetMetalInformation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SheetMetalInformation.md) must be true to access the sheet-metal definition of the mirrored sheet-metal part. Editing the sheet-metal definition updates [cut-list properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CutListProperties.md).

Example

[Mirror Sheet-metal Part (C#)](Mirror_Sheet-metal_Part_Example_CSharp.htm)  
[Mirror Sheet-metal Part (VB.NET)](Mirror_Sheet-metal_Part_Example_VBNET.htm)  
[Mirror Sheet-metal Part (VBA)](Mirror_Sheet-metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.md)
