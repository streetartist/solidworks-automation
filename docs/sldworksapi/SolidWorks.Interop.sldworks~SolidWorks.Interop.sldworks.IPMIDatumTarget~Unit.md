# Unit Property (IPMIDatumTarget)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Unit`

Gets the units for the values of this PMI datum target.
Gets the units for the values of this PMI datum target.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Unit As System.Integer
```

```

Dim instance As IPMIDatumTarget
Dim value As System.Integer
 
instance.Unit = value
 
value = instance.Unit
```

```

System.int Unit {get; set;}
```

```

property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Units as defined in [swPMIUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIUnit_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.md)  
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.md)  
[IPMIDatumTarget::Diameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Diameter.md)  
[IPMIDatumTarget::Height Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Height.md)  
[IPMIDatumTarget::Width Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Width.md)  
**IPMIDatumTarget::DiameterPrecision Property ()**  
**IPMIDatumTarget::HeightPrecision Property ()**  
**IPMIDatumTarget::WidthPrecision Property ()**
