# DefineUserNotification Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineUserNotification`

Called by a SOLIDWORKS add-in, creates a user notification definition object.
Called by a SOLIDWORKS add-in, creates a user notification definition object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DefineUserNotification( _
   ByVal UniqueName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim UniqueName As System.String
Dim value As System.Object
 
value = instance.DefineUserNotification(UniqueName)
```

```

System.object DefineUserNotification( 
   System.string UniqueName
)
```

```

System.Object^ DefineUserNotification( 
   System.String^ UniqueName
) 
```

#### Parameters

*UniqueName*
:   Unique ID of this user notification

#### Return Value

[IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.md)

Remarks

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique notification identifier:

"MyAddInName+ID\_MYNOTIFICATION1"

Example

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
