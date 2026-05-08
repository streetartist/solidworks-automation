# XorHighlight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~XorHighlight`

Gets or sets the Xor highlight state.
Gets or sets the Xor highlight state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property XorHighlight As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.XorHighlight = value
 
value = instance.XorHighlight
```

```

System.bool XorHighlight {get; set;}
```

```

property System.bool XorHighlight {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to Xor the hightlight state, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
