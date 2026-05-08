# ResponseAText Property (IUserNotificationDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseAText`

Gets or sets the text displayed on the first button or command link of this user notification.
Gets or sets the text displayed on the first button or command link of this user notification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ResponseAText As System.String
```

```

Dim instance As IUserNotificationDefinition
Dim value As System.String
 
instance.ResponseAText = value
 
value = instance.ResponseAText
```

```

System.string ResponseAText {get; set;}
```

```

property System.String^ ResponseAText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text displayed on first user response control; default is an empty string

Example

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)  
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.md)
