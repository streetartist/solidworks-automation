# SetValues Method (IMateControllerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~SetValues`

Sets the mate values for the specified mate position.
Sets the mate values for the specified mate position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetValues( _
   ByVal PositionName As System.String, _
   ByVal Values As System.Object _
) 
```

```

Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim Values As System.Object
 
instance.SetValues(PositionName, Values)
```

```

void SetValues( 
   System.string PositionName,
   System.object Values
)
```

```

void SetValues( 
   System.String^ PositionName,
   System.Object^ Values
) 
```

#### Parameters

*PositionName*
:   Name of mate position

*Values*
:   Array of values for all mates in PositionName

Remarks

The number of items in Values must correspond to the number of mates passed to [IMateControllerFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.md) or the number of pre-selected mates.

Example

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
