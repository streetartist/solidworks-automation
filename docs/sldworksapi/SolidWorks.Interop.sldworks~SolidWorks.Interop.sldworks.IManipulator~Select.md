# Select Method (IManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Select`

Select a manipulator.
Select a manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As IManipulator
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select(Append, Data)
```

```

System.bool Select( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends the manipulator tot he selection list, false replaces the selection list with this manipulator

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the manipulator is selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
