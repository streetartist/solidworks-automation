# GeometricCharacteristic Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic`

Gets the geometric characteristic of this Gtol frame.
Gets the geometric characteristic of this Gtol frame.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GeometricCharacteristic As System.Integer
```

```

Dim instance As IPMIFrameData
Dim value As System.Integer
 
instance.GeometricCharacteristic = value
 
value = instance.GeometricCharacteristic
```

```

System.int GeometricCharacteristic {get; set;}
```

```

property System.int GeometricCharacteristic {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Geometric characteristic as defined in [swGeometricCharacteristic\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.md)  
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.md)
