# SetDisplayMode2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode2`

Obsolete. Superseded by IView::SetDisplayMode3.
Obsolete. Superseded by [IView::SetDisplayMode3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplayMode2( _
   ByVal Mode As System.Integer, _
   ByVal Facetted As System.Boolean, _
   ByVal Edges As System.Boolean _
) As System.Boolean
```

```

Dim instance As IView
Dim Mode As System.Integer
Dim Facetted As System.Boolean
Dim Edges As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDisplayMode2(Mode, Facetted, Edges)
```

```

System.bool SetDisplayMode2( 
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
)
```

```

System.bool SetDisplayMode2( 
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
) 
```

#### Parameters

*Mode*

*Facetted*

*Edges*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
