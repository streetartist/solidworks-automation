# DisableAutoUpdate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~DisableAutoUpdate`

Gets or sets whether to disable the automatic update of this view.
Gets or sets whether to disable the automatic update of this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisableAutoUpdate As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.DisableAutoUpdate = value
 
value = instance.DisableAutoUpdate
```

```

System.bool DisableAutoUpdate {get; set;}
```

```

property System.bool DisableAutoUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to disable the automatic update, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
