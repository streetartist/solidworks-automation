# GetValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~GetValues`

Gets the mate values for the specified mate position.
Gets the mate values for the specified mate position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetValues( _
   ByVal PositionName As System.String _
) As System.Object
```

```

Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim value As System.Object
 
value = instance.GetValues(PositionName)
```

```

System.object GetValues( 
   System.string PositionName
)
```

```

System.Object^ GetValues( 
   System.String^ PositionName
) 
```

#### Parameters

*PositionName*
:   Name of mate position

#### Return Value

Array of values for all mates in PositionName

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
