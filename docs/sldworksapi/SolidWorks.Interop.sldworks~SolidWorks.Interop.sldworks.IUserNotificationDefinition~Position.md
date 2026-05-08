# Position Property (IUserNotificationDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Position`

Gets or sets the relative position of this user notification within the parent window.
Gets or sets the relative position of this user notification within the parent window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As System.Integer
```

```

Dim instance As IUserNotificationDefinition
Dim value As System.Integer
 
instance.Position = value
 
value = instance.Position
```

```

System.int Position {get; set;}
```

```

property System.int Position {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Position as defined by [swUserNotificationPosition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationPosition_e.html)

Remarks

Default value of this property is swUserNotificationPosition\_e.swUserNotificationPosition\_Default.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)  
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.md)
