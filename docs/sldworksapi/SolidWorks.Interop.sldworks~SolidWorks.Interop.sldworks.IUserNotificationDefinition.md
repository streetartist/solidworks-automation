# IUserNotificationDefinition Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition`

Allows access to a user notification of an add-in.
Allows access to a user notification of an add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IUserNotificationDefinition 
```

```

Dim instance As IUserNotificationDefinition
```

```

public interface IUserNotificationDefinition 
```

```

public interface class IUserNotificationDefinition 
```

Remarks

A user notification is an add-in dialog that:

- Allows an add-in to display a unique message to SOLIDWORKS users.
- Is modeless.
- May appear within the context of a document open in its own frame or within SOLIDWORKS itself.
- Replaces any previously displayed user notification.
- Requires an IUserNotificationHandler to handle user notification events.

Example

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)
