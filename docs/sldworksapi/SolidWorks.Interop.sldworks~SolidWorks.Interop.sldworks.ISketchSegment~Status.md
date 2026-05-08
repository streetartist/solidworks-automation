# Status Property (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Status`

Gets the constraint status for this sketch segment.
Gets the constraint status for this sketch segment.

**NOTE: This property is a get-only property. Set is not implemented.**

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Status As System.Integer
```

```

Dim instance As ISketchSegment
Dim value As System.Integer
 
instance.Status = value
 
value = instance.Status
```

```

System.int Status {get; set;}
```

```

property System.int Status {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Sketch segment constraint status as defined in [swConstrainedStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedStatus_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
