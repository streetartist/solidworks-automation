# GetDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetDirection`

Gets the rip direction for the specified edge.
Gets the rip direction for the specified edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDirection( _
   ByVal Edge As System.Object _
) As System.Integer
```

```

Dim instance As IRipFeatureData
Dim Edge As System.Object
Dim value As System.Integer
 
value = instance.GetDirection(Edge)
```

```

System.int GetDirection( 
   System.object Edge
)
```

```

System.int GetDirection( 
   System.Object^ Edge
) 
```

#### Parameters

*Edge*
:   [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

Direction of the rip feature for the specified edge:

- 0 = this direction
- 1 = other direction
- 2 = both directions

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md)  
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.md)  
[IRipFeatureData::SetDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~SetDirection.md)
