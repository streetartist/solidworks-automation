# AddNewPosition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AddNewPosition`

Adds a mate position name to this mate controller.
Adds a mate position name to this mate controller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddNewPosition( _
   ByVal PositionName As System.String _
) As System.Boolean
```

```

Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim value As System.Boolean
 
value = instance.AddNewPosition(PositionName)
```

```

System.bool AddNewPosition( 
   System.string PositionName
)
```

```

System.bool AddNewPosition( 
   System.String^ PositionName
) 
```

#### Parameters

*PositionName*
:   Name of mate position to add

#### Return Value

True if mate position successfully created, false if not

Example

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
