# UpdatePosition Method (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition`

Obsolete. Superseded by Callout::Position.
Obsolete. Superseded by [Callout::Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Position.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UpdatePosition( _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) 
```

```

Dim instance As ICallout
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
 
instance.UpdatePosition(XPos, YPos, ZPos)
```

```

void UpdatePosition( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

```

void UpdatePosition( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
) 
```

#### Parameters

*XPos*
:   x coordinate for callout

*YPos*
:   y coordinate for callout

*ZPos*
:   z coordinate for callout

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)
