# AddConfigurationFromPosition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AddConfigurationFromPosition`

Adds a configuration from the specified mate position.
Adds a configuration from the specified mate position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConfigurationFromPosition( _
   ByVal PositionName As System.String, _
   ByVal IsUpdate As System.Boolean _
) As System.Boolean
```

```

Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim IsUpdate As System.Boolean
Dim value As System.Boolean
 
value = instance.AddConfigurationFromPosition(PositionName, IsUpdate)
```

```

System.bool AddConfigurationFromPosition( 
   System.string PositionName,
   System.bool IsUpdate
)
```

```

System.bool AddConfigurationFromPosition( 
   System.String^ PositionName,
   System.bool IsUpdate
) 
```

#### Parameters

*PositionName*
:   Name of mate position

*IsUpdate*
:   True if an update, false if not

#### Return Value

True if configuration successfully added, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
