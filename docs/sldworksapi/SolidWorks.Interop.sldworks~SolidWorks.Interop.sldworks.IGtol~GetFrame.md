# GetFrame Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrame`

Gets the Gtol frame at the specified index.
Gets the Gtol frame at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrame( _
   ByVal FrameIndex As System.Integer _
) As System.Object
```

```

Dim instance As IGtol
Dim FrameIndex As System.Integer
Dim value As System.Object
 
value = instance.GetFrame(FrameIndex)
```

```

System.object GetFrame( 
   System.int FrameIndex
)
```

```

System.Object^ GetFrame( 
   System.int FrameIndex
) 
```

#### Parameters

*FrameIndex*
:   One-based index of Gtol frame to retrieve

#### Return Value

[IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md)

Remarks

This method is valid only if this Gtol was created in SOLIDWORKS 2022 or later.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
