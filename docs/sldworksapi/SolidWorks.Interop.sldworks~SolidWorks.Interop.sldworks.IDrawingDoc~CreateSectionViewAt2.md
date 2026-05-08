# CreateSectionViewAt2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt2`

Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt4.
Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSectionViewAt2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal IsOffsetSection As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Chgdirection As System.Boolean, _
   ByVal Scwithmodel As System.Boolean, _
   ByVal Partial As System.Boolean, _
   ByVal Dispsurfcut As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim IsOffsetSection As System.Boolean
Dim Label As System.String
Dim Chgdirection As System.Boolean
Dim Scwithmodel As System.Boolean
Dim Partial As System.Boolean
Dim Dispsurfcut As System.Boolean
Dim value As System.Object
 
value = instance.CreateSectionViewAt2(X, Y, Z, NotAligned, IsOffsetSection, Label, Chgdirection, Scwithmodel, Partial, Dispsurfcut)
```

```

System.object CreateSectionViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.string Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut
)
```

```

System.Object^ CreateSectionViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.String^ Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut
) 
```

#### Parameters

*X*

*Y*

*Z*

*NotAligned*

*IsOffsetSection*

*Label*

*Chgdirection*

*Scwithmodel*

*Partial*

*Dispsurfcut*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
