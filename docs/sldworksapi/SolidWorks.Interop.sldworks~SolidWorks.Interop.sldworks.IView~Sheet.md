# Sheet Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Sheet`

Gets the sheet on which this drawing view exists.
Gets the sheet on which this drawing view exists.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Sheet As Sheet
```

```

Dim instance As IView
Dim value As Sheet
 
value = instance.Sheet
```

```

Sheet Sheet {get;}
```

```

property Sheet^ Sheet {
   Sheet^ get();
}
```

#### Property Value

[Sheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
