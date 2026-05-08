# SetHoleLocationPrecision Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~SetHoleLocationPrecision`

Sets the precision to use for location values for this hole table.
Sets the precision to use for location values for this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetHoleLocationPrecision( _
   ByVal UseDoc As System.Boolean, _
   ByVal Precision As System.Integer _
) As System.Boolean
```

```

Dim instance As IHoleTable
Dim UseDoc As System.Boolean
Dim Precision As System.Integer
Dim value As System.Boolean
 
value = instance.SetHoleLocationPrecision(UseDoc, Precision)
```

```

System.bool SetHoleLocationPrecision( 
   System.bool UseDoc,
   System.int Precision
)
```

```

System.bool SetHoleLocationPrecision( 
   System.bool UseDoc,
   System.int Precision
) 
```

#### Parameters

*UseDoc*
:   True to set the location for this hole table using the document's precision, false  
    to not

*Precision*
:   Precision to use for location values if UseDoc set to false

#### Return Value

True if precision is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::GetHoleLocationPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationPrecision.md)  
[IHoleTable::GetHoleLocationUseDocPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationUseDocPrecision.md)
