# CreateText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText`

Obsolete. Superseded by IDrawingDoc::CreateText2.
Obsolete. Superseded by [IDrawingDoc::CreateText2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateText( _
   ByVal TextString As System.String, _
   ByVal TextX As System.Double, _
   ByVal TextY As System.Double, _
   ByVal TextZ As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal TextAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim TextString As System.String
Dim TextX As System.Double
Dim TextY As System.Double
Dim TextZ As System.Double
Dim TextHeight As System.Double
Dim TextAngle As System.Double
Dim value As System.Boolean
 
value = instance.CreateText(TextString, TextX, TextY, TextZ, TextHeight, TextAngle)
```

```

System.bool CreateText( 
   System.string TextString,
   System.double TextX,
   System.double TextY,
   System.double TextZ,
   System.double TextHeight,
   System.double TextAngle
)
```

```

System.bool CreateText( 
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

*TextX*

*TextY*

*TextZ*

*TextHeight*

*TextAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
