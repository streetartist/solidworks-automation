# IMessageBarDefinition Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition`

Allows access to a message bar in an add-in.
Allows access to a message bar in an add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMessageBarDefinition 
```

```

Dim instance As IMessageBarDefinition
```

```

public interface IMessageBarDefinition 
```

```

public interface class IMessageBarDefinition 
```

Remarks

A message bar:

- Allows an add-in to display a message to users.
- Is a modeless dialog that contains a unique message.
- Only appears within the context of a document open in its own frame.
- May be stacked with other message bars in the user interface.
- Requires an IMessageBarHandler to handle message bar events.

Example

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)
