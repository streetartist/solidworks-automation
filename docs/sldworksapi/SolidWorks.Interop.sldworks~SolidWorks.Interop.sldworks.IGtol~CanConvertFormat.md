# CanConvertFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~CanConvertFormat`

Gets whether this Gtol can be converted to the current format.
Gets whether this Gtol can be converted to the current format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CanConvertFormat() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.CanConvertFormat()
```

```

System.bool CanConvertFormat()
```

```

System.bool CanConvertFormat(); 
```

#### Return Value

True if can be converted, false if not

Remarks

If this method returns true, call [IGtol::ConvertFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~ConvertFormat.md) to convert the Gtol to the current format.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
