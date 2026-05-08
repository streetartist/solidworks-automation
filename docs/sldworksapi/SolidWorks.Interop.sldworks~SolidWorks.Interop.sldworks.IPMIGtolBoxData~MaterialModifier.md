# MaterialModifier Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~MaterialModifier`

Gets the material condition for this PMI Gtol frame box.
Gets the material condition for this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialModifier As System.Integer
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Integer
 
instance.MaterialModifier = value
 
value = instance.MaterialModifier
```

```

System.int MaterialModifier {get; set;}
```

```

property System.int MaterialModifier {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Material condition as defined in [swMaterialModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html) (see Remarks)

Remarks

All material conditions in swMaterialModifier\_e are valid except swMaterialModifier\_e.swMaterialModifier\_Translation.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)  
[IPMIGtolBoxData::GetAdditionalSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetAdditionalSymbols.md)
