# ICreateSectionViewAt3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt3`

Obsolete. Superseded by IDrawingDoc::ICreateSectionViewAt4.
Obsolete. Superseded by [IDrawingDoc::ICreateSectionViewAt4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSectionViewAt3( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal IsOffsetSection As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Chgdirection As System.Boolean, _
   ByVal Scwithmodel As System.Boolean, _
   ByVal Partial As System.Boolean, _
   ByVal Dispsurfcut As System.Boolean, _
   ByVal NumExcludedComponents As System.Integer, _
   ByRef PExcludedComponents As System.Object _
) As View
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
Dim NumExcludedComponents As System.Integer
Dim PExcludedComponents As System.Object
Dim value As View
 
value = instance.ICreateSectionViewAt3(X, Y, Z, NotAligned, IsOffsetSection, Label, Chgdirection, Scwithmodel, Partial, Dispsurfcut, NumExcludedComponents, PExcludedComponents)
```

```

View ICreateSectionViewAt3( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.string Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut,
   System.int NumExcludedComponents,
   ref System.object PExcludedComponents
)
```

```

View^ ICreateSectionViewAt3( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.String^ Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut,
   System.int NumExcludedComponents,
   System.Object^% PExcludedComponents
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

*NumExcludedComponents*

*PExcludedComponents*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
