# CloseMessageBar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CloseMessageBar`

Closes the specified message bar in this document's window.
Closes the specified message bar in this document's window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CloseMessageBar( _
   ByVal Handler As System.Object _
) 
```

```

Dim instance As IModelDocExtension
Dim Handler As System.Object
 
instance.CloseMessageBar(Handler)
```

```

void CloseMessageBar( 
   System.object Handler
)
```

```

void CloseMessageBar( 
   System.Object^ Handler
) 
```

#### Parameters

*Handler*
:   [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
