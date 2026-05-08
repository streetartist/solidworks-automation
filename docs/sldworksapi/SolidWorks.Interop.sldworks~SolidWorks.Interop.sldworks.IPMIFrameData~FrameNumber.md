# FrameNumber Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~FrameNumber`

Gets the index of this Gtol frame.
Gets the index of this Gtol frame.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameNumber As System.Integer
```

```

Dim instance As IPMIFrameData
Dim value As System.Integer
 
instance.FrameNumber = value
 
value = instance.FrameNumber
```

```

System.int FrameNumber {get; set;}
```

```

property System.int FrameNumber {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Zero-based index of this Gtol frame

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.md)  
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.md)
