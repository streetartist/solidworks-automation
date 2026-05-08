# IGetXAxisEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities`

Gets the entities for the x axis of this coordinate system feature.
Gets the entities for the x axis of this coordinate system feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetXAxisEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ICoordinateSystemFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetXAxisEntities(Count)
```

```

System.object IGetXAxisEntities( 
   System.int Count
)
```

```

System.Object^ IGetXAxisEntities( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of entites for the x axis

#### Return Value

- in-process, unmanaged C++: Pointer to an an array of entities for the x axis

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ICoordinateSystemFeatureData::GetXAxisEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.md) before calling this method to get Count.

See SOLIDWORKS Help for a list of valid entities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.md)  
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.md)  
[ICoordinateSystemFeatureData::ISetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.md)  
[ICoordinateSystemFeatureData::XAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XAxisEntities.md)  
[ICoordinateSystemFeatureData::XFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XFlipped.md)  
[ICoordinateSystemFeatureData::GetXAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.md)  
[ICoordinateSystemFeatureData::GetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.md)  
[ICoordinateSystemFeatureData::IGetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntitiesTypes.md)
