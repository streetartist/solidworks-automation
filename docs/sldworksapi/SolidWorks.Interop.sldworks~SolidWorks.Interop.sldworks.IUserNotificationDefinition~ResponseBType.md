# ResponseBType Property (IUserNotificationDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseBType`

Gets or sets the second response user control for this message bar.
Gets or sets the second response user control for this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ResponseBType As System.Integer
```

```

Dim instance As IUserNotificationDefinition
Dim value As System.Integer
 
instance.ResponseBType = value
 
value = instance.ResponseBType
```

```

System.int ResponseBType {get; set;}
```

```

property System.int ResponseBType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Second response user control as defined by [swUserNotificationResponseType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationResponseType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)  
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.md)
