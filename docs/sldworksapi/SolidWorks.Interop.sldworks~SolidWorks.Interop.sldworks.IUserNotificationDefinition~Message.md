# Message Property (IUserNotificationDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Message`

Gets or sets the message displayed on this message bar.
Gets or sets the message displayed on this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Message As System.String
```

```

Dim instance As IUserNotificationDefinition
Dim value As System.String
 
instance.Message = value
 
value = instance.Message
```

```

System.string Message {get; set;}
```

```

property System.String^ Message {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Non-empty message string

Remarks

This property must be set.

Example

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)  
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.md)
