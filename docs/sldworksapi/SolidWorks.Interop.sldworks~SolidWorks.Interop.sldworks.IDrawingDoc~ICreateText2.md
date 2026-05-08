# ICreateText2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2`

Creates a note containing the specified text at a given location.
Creates a [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) containing the specified text at a given location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateText2( _
   ByVal TextString As System.String, _
   ByVal TextX As System.Double, _
   ByVal TextY As System.Double, _
   ByVal TextZ As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal TextAngle As System.Double _
) As Note
```

```

Dim instance As IDrawingDoc
Dim TextString As System.String
Dim TextX As System.Double
Dim TextY As System.Double
Dim TextZ As System.Double
Dim TextHeight As System.Double
Dim TextAngle As System.Double
Dim value As Note
 
value = instance.ICreateText2(TextString, TextX, TextY, TextZ, TextHeight, TextAngle)
```

```

Note ICreateText2( 
   System.string TextString,
   System.double TextX,
   System.double TextY,
   System.double TextZ,
   System.double TextHeight,
   System.double TextAngle
)
```

```

Note^ ICreateText2( 
   System.String^ TextString,
   System.double TextX,
   System.double TextY,
   System.double TextZ,
   System.double TextHeight,
   System.double TextAngle
) 
```

#### Parameters

*TextString*
:   User input text

*TextX*
:   X text location in meters (see **Remarks**)

*TextY*
:   Y text location in meters (see Remarks)

*TextZ*
:   Z text location in meters (see Remarks)

*TextHeight*
:   Text height in meters

*TextAngle*
:   Text angle for rotated text in radians

#### Return Value

Pointer to the [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

The location specifies the position of the upper-left corner of the box containing the text with respect to the lower-left corner of the drawing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md)
