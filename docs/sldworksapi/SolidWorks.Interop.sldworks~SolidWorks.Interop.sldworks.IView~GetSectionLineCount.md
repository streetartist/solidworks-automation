# GetSectionLineCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount`

Obsolete. Superseded by IView::GetSectionLineCount2.
Obsolete. Superseded by [IView::GetSectionLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionLineCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetSectionLineCount(Size)
```

```

System.int GetSectionLineCount( 
   out System.int Size
)
```

```

System.int GetSectionLineCount( 
   [Out] System.int Size
) 
```

#### Parameters

*Size*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
