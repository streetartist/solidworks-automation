# CloseUserNotification Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseUserNotification`

Closes the specified user notification.
Closes the specified user notification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CloseUserNotification( _
   ByVal Definition As System.Object _
) 
```

```

Dim instance As ISldWorks
Dim Definition As System.Object
 
instance.CloseUserNotification(Definition)
```

```

void CloseUserNotification( 
   System.object Definition
)
```

```

void CloseUserNotification( 
   System.Object^ Definition
) 
```

#### Parameters

*Definition*
:   [IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
