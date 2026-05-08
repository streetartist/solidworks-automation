# IGetTessTriStripSize Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripSize`

Gets the array size of floats required to contain the data returned when calling IComponent2::IGetTessTriStrips.
Gets the array size of floats required to contain the data returned when calling [IComponent2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStrips.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessTriStripSize() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.IGetTessTriStripSize()
```

```

System.int IGetTessTriStripSize()
```

```

System.int IGetTessTriStripSize(); 
```

#### Return Value

Size of the array

Remarks

Tessellation information is available only when the component is loaded as lightweight.

SOLIDWORKS calculates this number as ( 3 + FaceCount + StripCount + 3 \* VertexCount).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
