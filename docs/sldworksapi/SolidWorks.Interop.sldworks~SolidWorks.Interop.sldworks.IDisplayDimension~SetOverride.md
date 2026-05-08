# SetOverride Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOverride`

Sets whether to display the actual dimension value or to display another value, and, if so, that value.
Sets whether to display the actual dimension value or to display another value, and, if so, that value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverride( _
   ByVal Override As System.Boolean, _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Override As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetOverride(Override, Value)
```

```

System.bool SetOverride( 
   System.bool Override,
   System.double Value
)
```

```

System.bool SetOverride( 
   System.bool Override,
   System.double Value
) 
```

#### Parameters

*Override*
:   True to display a value other than the actual dimension value, false to display the actual value

*Value*
:   Value to display instead of the actual dimension value

#### Return Value

True if setting an override value is successful, false if not

Remarks

This method can only be used on a display dimension in a drawing. In a part or assembly, this method takes no action and returns false.

If Override is set to false, then the Value argument is ignored.

Use [IDisplayDimension::GetOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverride.md) to get whether the actual dimension value or another value is displayed.   

Use [IDisplayDimension::GetOverrideValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverrideValue.md) to get the value to display instead of the actual dimension value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
