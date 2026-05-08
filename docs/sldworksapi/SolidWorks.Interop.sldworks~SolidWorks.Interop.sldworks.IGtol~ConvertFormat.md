# ConvertFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~ConvertFormat`

Converts this Gtol to the current format.
Converts this Gtol to the current format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertFormat() As System.Integer
```

```

Dim instance As IGtol
Dim value As System.Integer
 
value = instance.ConvertFormat()
```

```

System.int ConvertFormat()
```

```

System.int ConvertFormat(); 
```

#### Return Value

0 if successfully converted, otherwise error code as defined by [swGtolFormatConversionError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatConversionError_e.html)

Remarks

Before calling this method, use [IGtol::CanConvertFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~CanConvertFormat.md) to determine whether conversion is possible.

If unsupported data are in this older Gtol, then this method will fail.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
