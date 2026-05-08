# ShowMessageBar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowMessageBar`

Shows the specified message bar in this document's window.
Shows the specified message bar in this document's window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowMessageBar( _
   ByVal Definition As System.Object, _
   ByVal Handler As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Definition As System.Object
Dim Handler As System.Object
Dim value As System.Integer
 
value = instance.ShowMessageBar(Definition, Handler)
```

```

System.int ShowMessageBar( 
   System.object Definition,
   System.object Handler
)
```

```

System.int ShowMessageBar( 
   System.Object^ Definition,
   System.Object^ Handler
) 
```

#### Parameters

*Definition*
:   [IMessageBarDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)

*Handler*
:   [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md)

#### Return Value

Result code as defined by [swShowMessageBarResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowMessageBarResult_e.html)

Remarks

This method is called by an add-in to display the specified message bar in this document's window.

Example

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
