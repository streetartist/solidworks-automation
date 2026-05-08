# SuppressState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SuppressState`

Gets or sets the view suppress state.
Gets or sets the view suppress state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SuppressState As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
instance.SuppressState = value
 
value = instance.SuppressState
```

```

System.int SuppressState {get; set;}
```

```

property System.int SuppressState {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

- NO\_SUPPRESS = 0
- HALF\_SUPPRESS = 1
- FULL\_SUPPRESS = 2

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IDrawingDoc::SuIppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.md)
