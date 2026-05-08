# Initialize Method (IMateControllerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize`

Initializes this mate controller with the specified mates.
Initializes this mate controller with the specified mates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Initialize( _
   ByVal Mates As System.Object _
) 
```

```

Dim instance As IMateControllerFeatureData
Dim Mates As System.Object
 
instance.Initialize(Mates)
```

```

void Initialize( 
   System.object Mates
)
```

```

void Initialize( 
   System.Object^ Mates
) 
```

#### Parameters

*Mates*
:   Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

Before calling this method, use [IAssemblyDoc::IsSupportedMatesAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable.md) and [IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.md) to determine appropriates mates with which to initialize this mate controller.

Mates passed to this method are given precedence over pre-selected mates. If this method is not called or invalid mates are passed to it, then pre-selected mates are used.

For .NET applications, you must marshal the Mates array to IDispatch object arrays before calling this method. See [IDispatch Object Arrays as Input in .NET](ms-its:sldworksapiprogguide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm).

Example

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
