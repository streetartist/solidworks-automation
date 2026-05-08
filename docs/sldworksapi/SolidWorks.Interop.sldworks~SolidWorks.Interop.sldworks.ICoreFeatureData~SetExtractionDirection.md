# SetExtractionDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~SetExtractionDirection`

Sets the entities that define the extraction direction of this core feature.
Sets the entities that define the extraction direction of this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetExtractionDirection( _
   ByVal PDir1 As System.Object, _
   ByVal PDir2 As System.Object _
) As System.Boolean
```

```

Dim instance As ICoreFeatureData
Dim PDir1 As System.Object
Dim PDir2 As System.Object
Dim value As System.Boolean
 
value = instance.SetExtractionDirection(PDir1, PDir2)
```

```

System.bool SetExtractionDirection( 
   System.object PDir1,
   System.object PDir2
)
```

```

System.bool SetExtractionDirection( 
   System.Object^ PDir1,
   System.Object^ PDir2
) 
```

#### Parameters

*PDir1*
:   Entity that defines the extraction direction (see **Remarks**)

*PDir2*
:   Entity that defines the extraction direction (see Remarks)

#### Return Value

True if the entities that define the extraction direction of this core feature are set, false if not

Remarks

The types of entities that define the extraction direction are:

- Face
- Plane
- Edge
- Vertex
- Sketch line
- Sketch point

There can be two entities because two sketch points can specify a direction.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)  
[ICoreFeatureData::GetExtractionDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~GetExtractionDirection.md)
