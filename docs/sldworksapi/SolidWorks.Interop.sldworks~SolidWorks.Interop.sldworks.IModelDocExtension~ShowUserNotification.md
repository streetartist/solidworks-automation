# ShowUserNotification Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowUserNotification`

Displays the specified user notfication for this document.
Displays the specified user notfication for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowUserNotification( _
   ByVal Definition As System.Object, _
   ByVal Handler As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Definition As System.Object
Dim Handler As System.Object
Dim value As System.Integer
 
value = instance.ShowUserNotification(Definition, Handler)
```

```

System.int ShowUserNotification( 
   System.object Definition,
   System.object Handler
)
```

```

System.int ShowUserNotification( 
   System.Object^ Definition,
   System.Object^ Handler
) 
```

#### Parameters

*Definition*
:   [IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)

*Handler*
:   [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md)

#### Return Value

Result code as defined by [swShowNotificationResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowNotificationResult_e.html)

Example

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
