# SheetMetalInformation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SheetMetalInformation`

Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part.
Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SheetMetalInformation As System.Boolean
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean
 
instance.SheetMetalInformation = value
 
value = instance.SheetMetalInformation
```

```

System.bool SheetMetalInformation {get; set;}
```

```

property System.bool SheetMetalInformation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part, false to not

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
[IMirrorPartFeatureData::UnlockedProperties Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnlockedProperties.md)
